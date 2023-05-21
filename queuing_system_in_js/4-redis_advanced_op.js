import {createClient} from "redis";

const client = createClient();

client.on('error', err => {
  console.log('Redis client not connected to the server: ', err);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const values = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
}

for (const [key, val] of Object.entries(values)) {
  client.hset('HolbertonSchools', key, val, (error, reply) =>
      redis.print(('Reply:' + reply))
  );
}