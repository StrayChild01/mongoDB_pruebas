//
//    Este es un script de prueba para ver si funcionan estas co
//

use mi_script;
//selecciona el esquema, si no existe, lo crea.
db.miprueba.drop();
db.createCollection("miprueba");
//selecciona el esquema, si no existe, lo crea.

db.miprueba.insertOne({"name":"Ana", "age": 34, "alias": "aniuxa"});
// si no se inserta el campo _id, lo inserta automáticamente.

db.miprueba.insertMany(
  [
    {_id : 1, name:"usuario", age: 36, alias: "username"},
    //primer registro
    {_id : 2, name:"Ana", age: 34, alias:"aniuxa"},
    //segundo registro
    {_id : 3, name:"StrayChild01", age: 99, alias: "straychild01"},
    //tercer registro
    {_id : 4, name:"Juan", age:99, alias:"juanperez"},
    //cuarto registro
    {_id : 5, name:"OtherUser", age:-1, alias:"otheruser", phone: [ { home :  12345678, zip : 1234 } , { office : 987654321, zip : 444 } ] }
    //cuarto registro
  ]
);

db.miprueba.find();
//select * from miprueba

db.miprueba.find(
// select name, alias from miprueba where name = 'juan'
    { name: "juan"},
    //filter by value
    { name: 1, alias: 1, _id: 0 }
    // field list where 0 is to hide, 1 to show
);

db.miprueba.updateOne( {_id : 5}, { $set : {"name": "Ana", "age": 34, "alias":"aniuxa"} });
//$set se usa para actualizar varios campos.

db.miprueba.deleteMany( { alias: "otheruser" } );