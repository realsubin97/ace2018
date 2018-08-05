
var mongoose=require('mongoose');
/*db에 필요한 라우터
var member=require('../routes/member_route');
var medicine=require('../routes/medicine_route');*/

var database;
var testSchema;
var testModel;

var connectDB =function connectDB(){
    var databaseUrl="mongodb://localhost:27017/acedb";

    console.log('데이터베이스에 연결 시도!!');
    mongoose.connect(databaseUrl);
    database=mongoose.connection;

    database.on('error',console.error.bind(console,'mongoose connection error'));

    database.on('open',function(){
        console.log('데이터 베이스에 연결되었습니다. : '+databaseUrl);
        createTestSchema();
    });

    database.on('disconnected',function(){
        console.log('연결이 끊어졌습니다. 5초 후 다시 연결합니다.');
        setInterval(connectDB,5000);
    });
}
function creaTetestSchema(){
    testSchema=require('../database/testSchema').createSchema(mongoose);

    testModel=mongoose.model('test',testSchema);
    console.log('TestModel 정의함');

    test.init(database,testSchema,testModel);
}


module.exports=connectDB;
