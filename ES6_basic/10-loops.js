export default function appendToEachArrayValue(array, appendString) {
  const pepe = [];
  for (const idx of array) {
    pepe.push(`${appendString}${idx}`);
  }

  return pepe;
}
