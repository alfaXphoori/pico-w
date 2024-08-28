const { MongoClient } = require('mongodb');

// Replace the uri string with your MongoDB deployment's connection string.
const uri = "mongodb+srv://user:password@cluster0.ngazyzj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

// Create a new client and connect to MongoDB
const client = new MongoClient(uri);

async function run() {
  try {
    // Connect to the "insertDB" database and access its "haiku" collection
    const database = client.db("CeDB");
    const collects = database.collection("PicoW");
    
    // Create a document to insert
    const doc = {
      DeviceID: 104,
      Info: "Hi MongoDB",
    }
    // Insert the defined document into the "haiku" collection
    const result = await collects.insertOne(doc);

    // Print the ID of the inserted document
    console.log(`A document was inserted with the _id: ${result.insertedId}`);
  } finally {
     // Close the MongoDB client connection
    await client.close();
  }
}
// Run the function and handle any errors
run().catch(console.dir);
