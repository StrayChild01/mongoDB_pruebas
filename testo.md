Process Flow
Check if datastage is currently processing any Wafer load jobs  (query TBD  )
If nothing is running then continue, if datastage is already processing a Wafer load job then write message to log and exit

If running in normal mode then check all datasources for new data

 - Process datasource='WAF_SUPDLY'
   - Check if there is new data to process by comparing the source table timestamp with the BOWCTRL.LASTRUN table
    
    ```sql
        SELECT max(BOW_LOADDATE) as MAX_BOW_LOADDATE
        from BOWDLY.GF_ORDERS
    ```
    ```sql
        SELECT LASTROWTS
        FROM BOWCTRL.LASTRUN
        WHERE schemaname = 'BOWDLY'
            AND tbname = 'GF_ORDERS'
            AND process = 'WAFSUPDLY'
    ```

   - Write the timestamps to the log
   - If MAX_BOW_LOADDATE > LASTROWTS then there is new data
    Retrieve the next version to be processed
    ```sql
    SELECT min(version_id) AS version_id
    FROM BOWDLY.GF_ORDERS
    WHERE version_id >= (
            SELECT max(version_id)
            FROM BOWREP.EVENTS_VIEW
            WHERE event_process = 'BOW'
                AND BOWETL_WAFSUPDLY_COMPLETE IS NOT NULL
            )
    ```
    (Note: we use >= instead of > in case the version was updated)"
   - Check to see if we have already tried to process this version
    ```sql
        SELECT count(*)
        FROM BOW.DATASOURCE
        WHERE datasource = 'WAF_SUPDLY'
         AND version = 'version_id'

    ```
   - If count>0 then Write an informational message to the log 'This version &version_id already exists but the source has been updated re-processing'
   - Write an informational message to load showing the datasource, version, and runlist='SUPDLY'
   - Call datastage with datasource, version, and runlist to process
   - If Datastage completes successfully then _Call Blend Create/Update processing with Datasource, version_id, and runs to be processed_
   - If Datastage does not complete successfully then send an error email
   - Else no new supply daily data to process
        Write an informational message to log that there is no new data for this datasource.  (this is most common)

 - Process datasources 'CPE_WAF_QUAD2', 'CPE_WAF_SSP', 'CPE_WAF_TFF'
  
   - Check if there is new data according to the events table - (Note: for CPE datasources only the events table controls the run.  However, we check the LASTRUN timestamp and the datasource table for informational purposes.
        
        ```sql
            SELECT VERSION_ID AS event_version
                ,BOWREP_CAPONLY_COMPETE
                ,BOWETL_WAFQUAD2_COMPLETE
            FROM bowrep.events_view
            WHERE event_process = 'BOW'
                AND level_ind = (
                    SELECT min(level_ind)
                    FROM bowrep.events_view
                    WHERE event_process = 'BOW'
                    )

        ```

        Note:
        - for TFF use BOWREP_TFF_COMPLETE, BOWETL_WAFTFF_COMPLETE and event_process='TFF_BOW'
        - for SSP use BOWREP_SSP_COMPLETE, BOWETL_WAFSSP_COMPLETE and event_process='SSP_BOW'"
   - Write the event_version and timestamps to the log
   - If BOWREP_CAPONLY_COMPETE > BOWETL_WAFQUAD2_COMPLETE then there is new data in the repository
  
     - Retrieve the next version to be processed (in the case of backlog this may not always be equal to the most recent version in the events table

        ```sql
            SELECT coalesce(prior_version_id, curr_version_id)
            FROM (
                SELECT min(version_id) AS prior_version_id
                FROM bowrep.events_view b
                WHERE event_process = 'BOW'
                    AND BOWREP_CAPONLY_COMPLETE IS NOT NULL
                    AND BOWETL_WAFQUAD2_COMPLETE IS NULL
                    AND version_id >= (
                        SELECT max(version_id)
                        FROM bowrep.events_view
                        WHERE event_process = 'BOW'
                            AND NOT (BOWETL_WAFQUAD2_COMPLETE IS NULL)
                        )
                ) prior
                ,(
                    SELECT version_id AS curr_version_id
                    FROM bowrep.events_view
                    WHERE event_process = 'ACPE'
                        AND level_ind = 0
                    ) curr
        ```

    - For TFF use BOWREP_TFF_COMPLETE, BOWETL_WAFTFF_COMPLETE and event_process='TFF_BOW' and 'TFF_ACPE'
  
    - For SSP use BOWREP_SSP_COMPLETE, BOWETL_WAFSSP_COMPLETE and event_process='SSP_BOW' and 'SSP_ACPE'
   - Check to see if we have already tried to process this version
  
    ```sql
        SELECT count(*)
        FROM BOW.DATASOURCE
        WHERE datasource = & datasource
            AND version = & version_id
    ```
   - If count>0 then Write an informational message to the log ""This version &version_id already exists but the source has been updated - re-processing"" "
   - For informational purposes compare BOWCTRL.LASTRUN with the source
    ```sql
        SELECT max(LAST_UPDATE) AS MAX_LAST_UPDATE
        FROM BOWXXRAW.DEMPEG
        WHERE version_id = 'version_id'
    ```

    ```sql
        SELECT LASTROWTS
        FROM BOWCTRL.LASTRUN
        WHERE schemaname = 'BOWXXXRAW'
         AND tbname = 'DEMPEG'
         AND process = 'WAFSUPDMD'

    ```

    - Note: XXX='CPE', 'TFF', or 'SSP'"
  
   - If  MAX_LAST_UPDATE <= LASTROWTS then write a warning to the log that the source timestamp was not updated since the last time we loaded but the event timestamp changed.
   - Determine which supply runs are needed
   - If TFF or SSP then retrieve the run flags from the events table
    ```sql
        SELECT attribute_value AS RUNLIST
        --(this returns a string like ""CAP,UNL,OPP"")
        FROM bowrep.events
        WHERE event_process = 'TFF_ACPE'
            AND attribute_name LIKE 'TFF_COMPLETE%'
        ORDER BY version_id DESC
            --For SSP use SSP_ACPE, SSP_COMPLETE
    ```
   - Else
   - If QUAD2 then set RUNLIST = "CAP,FUN,OPP,RAW,UNL"
    - Write an informational message to the log showing the datasource, version, and runs to be processed
   - Call datastage with datasource, version, and runlist to process
   - If Datastage completes successfully then
     - Call Blend Create/Update processing with Datasource, version_id, and runs to be processed
   - If Datastage does not complete successfully then send an error email
     - Else no new event for this datasource - double check this is consistent with the BOWCTRL table
   - Double check this is consistent with the BOWCTRL table
    ```sql
        SELECT max(LAST_UPDATE) AS MAX_LAST_UPDATE
        FROM BOWXXRAW.DEMPEG
    ```
    ```sql
        SELECT LASTROWTS
        FROM BOWCTRL.LASTRUN
        WHERE schemaname = 'BOWXXXRAW'
            AND tbname = 'DEMPEG'
            AND process = 'WAFSUPDMD'
            --Note: XXX='CPE', 'TFF', or 'SSP'"
    ```
   - If  MAX_LAST_UPDATE > LASTROWTS then   - this is not quite right
   - Write timestamps to the log
   - Send a warning email with message "Source data appears to have been updated since the last time we loaded but the event timestamp was not updated.  Please check."
   - Else Write an informational message to log that there is no new data for this datasource.  (this is most common)
   - Process next datasource

If running in force mode then
- If datasource = 'WAF_SUPDLY' then
  - If version parameter is supplied then check that this is a valid version
      ```sql
          SELECT count(*)
          FROM bowdly.gf_orders
          WHERE version_id = 'version_id'
      ```
  - If count=0 then exit with error message indicating version is not valid
  - Else get the current version
      ```sql
          SELECT max(version_id)
          FROM bowdly.gf_orders
      ```
  - Write an informational message to load showing the datasource, version, and runlist='SUPDLY'
  - Call datastage with datasource, version, and runlist ='SUPDLY'
- Else  (QUAD2, SSP, TFF)
  - If version parameter is supplied then check that this is a valid version
    ```sql
        SELECT count(*)
        FROM bowrep.events_view
        WHERE event_process = 'BOW'
            AND version_id = 'version'
            AND BOWREP_CAPONLY_COMPLETE IS NOT NULL
    -- Note: For SSP use SSP_BOW and BOWREP_SSP_COMPLETE, For TFF use TFF_BOW and BOWREP_TFF_COMPLETE"
    ```
  - If count=0 then exit with error message indicating version is not valid
  - Else _Write an informational message to log showing the datasource, version, and runlist='SUPDLY'_
  - Call datastage with datasource, version, and runlist ='SUPDLY'
  - Else (version parameter is blank)
    - Retrieve the current version from the events table
    ```sql
        SELECT max(version_id)
        FROM bowrep.events_view
        WHERE event_process = 'BOW'
            AND BOWREP_CAPONLY_COMPLETE IS NOT NULL
        -- Note: For SSP use SSP_BOW and BOWREP_SSP_COMPLETE, For TFF use TFF_BOW and BOWREP_TFF_COMPLETE"
    ```
  - Write an informational message to log showing the datasource, version, and runlist='SUPDLY'
  - Call datastage with datasource, version, and runlist ='SUPDLY'
  - If Datastage completes successfully then
    - Call Blend Create/Update processing with Datasource, version, and runs to be processed
  - If Datastage does not complete successfully then send an error email
