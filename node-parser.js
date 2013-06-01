/**
 * XML parser for BCA data
 *
 * Install:
 * 1) Install MongoDB
 * 2) npm install xml-stream mongodb
 */

// Includes
var XMLStream = require('xml-stream');
var mongodb = require('mongodb');
var fs = require('fs');
var path = require('path');

// Top level variables
var dataPath = './data/BCACrimHistData/Files from BCA CD (Sept2012)/public.xml';
var count = 0;
var startDate = +new Date();

// Database
var db = new mongodb.Db('bca-db', new mongodb.Server('127.0.0.1', 27017, { w: 1 }));
db.open(function(err, dbClient) {
  dbClient.createCollection('bca', function(err, bcaCollection) {

    // Create stream
    var stream = fs.createReadStream(path.join(__dirname, dataPath));
    var xml = new XMLStream(stream);
    
    // Stream
    xml.preserve('item', true);
    xml.collect('subitem');
    xml.on('endElement: CriminalRecord', function(item) {
      count++;
      
      // Insert into collection
      bcaCollection.insert(item, function() {
        // Check for errors
      });
      
      // Some output
      if (count % 1000 === 0) {
        var endDate = +new Date();
        console.log('Records: ' + count + ' || Time (s): ' + ((endDate - startDate) / (1000)));
      }
    });
    
    // End
    xml.on('end', function(message) {
      var endDate = +new Date();
      console.log('Records: ' + count + ' || Time (s): ' + ((endDate - startDate) / (1000)));
    });
    
    // Error
    xml.on('error', function(message) {
    
    });
  });
});