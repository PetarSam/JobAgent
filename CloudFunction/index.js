const MongoClient = require('mongodb').MongoClient;
const uri = 'mongodb+srv://petarsam:'+ process.env.PASSWORD +'@cluster0-gp7st.gcp.mongodb.net/test?retryWrites=true&w=majority'

exports.mongoPost = (req, res) => {
  MongoClient.connect(uri,{
    useNewUrlParser: true,
    useUnifiedTopology: true
  }, 
  function(err, db) {
    if (err) throw err;
    var dbo = db.db("JobAgent");
    dbo.collection("agents").insertOne(JSON.parse(req.body), function(err, res) {
      if (err) throw err;
      res.status(200)
      db.close();
    });
  });
};


