export default function formatDuration(seconds) {
  if (!seconds) return "instant";
  let secs = seconds % 60;
  let mins = Math.floor(seconds / 60) % 60;
  let hours = Math.floor(seconds / (60 * 60)) % 24;
  let days = Math.floor(seconds / (24 * 60 * 60)) % 365;
  let years = Math.floor(seconds / (365 * 24 * 60 * 60));

  let time = [secs, mins, hours, days, years];
  for (let i = time.length - 1; i >= 0; i--) {
    if (time[i]) break;
    time.splice(i, 1);
  }
  const words = [" second", " minute", " hour", " day", " year"];
  for (let i = 0; i < time.length; i++) {
    if (time[i] > 1) {
      time[i] += words[i];
      time[i] += "s";
    } else {
      time[i] += words[i];
    }
  }
  time = time.filter((el) => +el[0]);
  return time.length > 2
    ? time
        .slice(2)
        .reverse()
        .map((el) => el + ", ")
        .join("") + time.slice(0, 2).reverse().join(" and ")
    : time.reverse().join(" and ");
}
