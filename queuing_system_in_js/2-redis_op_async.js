import {createClient, print} from "redis";
const { promisify } = require("util");

const client = createClient();
const get = promisify(client.get).bind(client);

client.on('error', err => {
  console.log('Redis client not connected to the server: ', err);
})

client.on('connect', () => {
  console.log('Redis client connected to the server');
})

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const value = await get(schoolName)
  console.log(value);
}

await displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');