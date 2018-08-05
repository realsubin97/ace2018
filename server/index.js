var http = require('http');
var express = require('express');
var bodyParser = require('body-parser');
var static = require('serve-static');
var path = require('path');
var session = require('express-session'); 


//db설정을 불러온다
var db = require('./config/db');

//express 객체 생성
var app = express();


//port라는 속성에 3000이라는 값을 설정
var port = process.env.PORT || 3000;


//ejs를 사용하기위해 view engine에 등록
app.set('view engine','ejs');
//view파일을 include 하기위해 사용
app.set('views', path.join(__dirname, 'views'));
 
//body본문의 파라미터를 받기위해서 미들웨어에 설정
app.use(bodyParser.urlencoded({extended : false}));
app.use(bodyParser.json());


//public폴더를 서버에서 사용하기 위한 설정
app.use('/public',static(path.join(__dirname,'public')));



//view 파일(.ejs)에서 사용할수 있도록 변수(currentUser)를 미들웨어에 전달
app.use(function(req,res,next){
   res.locals.isAuthenticated = req.isAuthenticated();
   res.locals.currentUser = req.user;
   next();
});



app.use('/',router); //경로에 /가 들어오면 router에서 경로를 잡게 한다.

//모든 경로에 대해 잘못된 경로로 접근시 처리
app.all('*', function(req, res) {
   res.status(401).send('<h1>잘못된 접근입니다.<br><a href="/home">홈페이지로 이동</a></h1>');
});


//서버시작과 함께 db설정 불러오기
http.createServer(app).listen(port,function(){

console.log('3000번 포트로 서버가 시작 되었습니다.');
pool.getConnection(function(err ,connection) {
   if (err) {
     console.log('Unable to connect to MySQL.');
     process.exit(1);
   }
   else
     console.log('database connected');
     connection.release();
  });
});

