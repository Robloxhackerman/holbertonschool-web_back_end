export default function returnHowManyArguments(...theArgs) {

  let total = 0;

  for (const args of theArgs) {
    total += args;
  }
  return total;
}
