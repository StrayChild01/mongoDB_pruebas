# Pruebas en mongo shell

Como base, estoy tomando los siguientes sitios [Cómo pasar de SQL a NoSQL sin sufrir]

[Cómo pasar de SQL a NoSQL sin sufrir]: https://medium.com/techwomenc/como-pasar-de-sql-a-nosql-sin-sufrir-e34dd22349e5
[segunda parte]: https://medium.com/techwomenc/como-pasar-de-sql-a-nosql-sin-sufrir-2-b072b98b258f

#### Para crear una DB
    use miprueba; //selecciona el esquema, si no existe, lo crea.
    
#### Para crear una tabla (en mongo son colecciones)
    db.createCollection("miprueba") //selecciona el esquema, si no existe, lo crea.
    
#### Para insertar un documento o varios.
    db.miprueba.insertOne({"name":"Ana", "age": 34, "alias": "aniuxa"});
    // si no se inserta el campo _id, lo inserta automáticamente.
    
    db.miprueba.insertMany(
      [
        {_id : 1, name:"Rancheri", age: 36, alias: "straychild01"}, //primer registro
        {_id : 9, name:"juan", age:99, alias:"juanperez"} //segundo registro
      ]
    );
    
#### Para seleccionar uno o varios documentos.
    db.miprueba.find(); //select * from miprueba
    
    db.miprueba.find(
    // select name, alias from miprueba where name = 'juan'
	    { name: "juan"},
	    //filter by value
	    { name: 1, alias: 1, _id: 0 }
	    // field list where 0 is to hide, 1 to show
    )
    
#### Para actualizar un documento o varios.
    db.miprueba.updateOne( {_id : 5}, { $set : {"name": "Ana", "age": 34, "alias":"aniuxa"} });
    //$set se usa para actualizar varios campos.
    
### Para eliminar documento
    db.miprueba.deleteMany( { alias: "aniuxa" } );
    
### Para eliminar una colección.
    db.students.drop()

### Para eliminar una base de datos.
    use miprueba;
    db.dropDatabase();
