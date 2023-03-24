export default function divideFunction(numerator, denominator) {
  let resultado = 0;

  if (denominator > 0) {
    resultado = numerator / denominator;
  } else {
    throw new Error('cannot divide by 0');
  }
  return resultado;
}
