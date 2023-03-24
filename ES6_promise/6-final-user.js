import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const promeson = { status: 'pending ' };
  const promesita = { status: 'pending ' };

  try {
    const signup = await signUpUser(firstName, lastName);
    promeson.status = 'fulfilled';
    promeson.value = signup;
  } catch (e) {
    promeson.status = 'rejected';
    promeson.value = e.toString();
  }

  try {
    const upload = await uploadPhoto(fileName);
    promesita.status = 'fulfilled';
    promesita.value = upload;
  } catch (e) {
    promesita.status = 'rejected';
    promesita.value = e.toString();
  }

  return [promeson, promesita];
}

export default handleProfileSignup;
