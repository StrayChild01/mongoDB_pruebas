CREATE TABLE
	america.tbl_gpfs_sequential_data (
		version text,
		operation_exec TIMESTAMP,
		operation_type text,
		proc_count INT,
		io_size INT,
		sample_cmmd text,
		lst_proc_date_rate LIST<FLOAT>,
		lst_proc_op_rate LIST<FLOAT>,
		lst_proc_avg_latency LIST<FLOAT>,
		lst_proc_bytes_transf LIST<FLOAT>,
		lst_proc_thread_util LIST<FLOAT>,
		average_data_rate FLOAT,
		status_report text,
		PRIMARY KEY ((version),operation_exec,operation_type,proc_count,io_size)
	) WITH CLUSTERING ORDER BY (operation_exec DESC,operation_type ASC,proc_count ASC,io_size ASC);
	
TRUNCATE america.tbl_gpfs_sequential_data;

insert into	america.tbl_gpfs_sequential_data(
	"version",
	"operation_exec",
	"operation_type",
	"proc_count",
	"io_size",
	"sample_cmmd",
	"lst_proc_date_rate",
	"lst_proc_op_rate",
	"lst_proc_avg_latency",
	"lst_proc_bytes_transf",
	"lst_proc_thread_util",
	"average_date_rate",
	"status_report"
)
values(
    '5.0.0.0',
    '2018-03-26 20:02:51.000-0400',
    'Sequential Buffered Write I/O',
    1,
    2048,
    $$mpiexec -f /mnt/sw_ppc64/mpich/mf.perf_ppc64.clients -n 1 /mnt/sw_ppc64/benchmarks/gpfsperf/gpfsperf-mpi write seq -repeat 5 -r \'2048\'k -n 64g -fsync /mnt/gpfs2a/gpfsperf_out/gpfsperfsfseq /mnt/sw_ppc64/benchmarks/gpfsperf/gpfsperf-mpi write seq /mnt/gpfs2a/gpfsperf_out/gpfsperfsfseq$$,
    [3169488.48, 3165907.81, 3163580.10, 3171726.08, 3163002.45],
    [1511.33, 1509.62, 1508.51, 1512.40, 1508.24],
    [0.656, 0.656, 0.655, 0.655, 0.657],
    [68719476736, 68719476736, 68719476736, 68719476736, 68719476736],
    [0.991, 0.991, 0.989, 0.990, 0.990],
    3166740.984, /*((3169488.48+3165907.81+3163580.10+3171726.08+3163002.45)/5)*/
    'processing'
);
/* valores tomados de archivo gpfsperf_buffered_write_2018-03-26-20_02_46.txt*/
	
	