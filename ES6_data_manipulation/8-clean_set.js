export default function cleanSet(set, startString) {
  if (!startString || !startString.length || typeof startString !== 'string') {
    return '';
  }

  let elString = '';

  set.forEach((element) => {
    if (element && element.startsWith(startString)) {
      elString += `${element.slice(startString.length)}-`;
    }
  });

  return elString.slice(0, elString.length - 1);
}
