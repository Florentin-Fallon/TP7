const socket = new WebSocket("ws://localhost:8765");

socket.addEventListener("open", (event) => {
  console.log("WebSocket connection opened!");

  const name = prompt("Comment tu t'appelle ?");
  socket.send(name);
  console.log(`>>> ${name}`);
  const string = prompt(`hello ${name} ! Quel est ton message ?`);
  socket.send(string);
  console.log(`>>> ${string}`);
});

socket.addEventListener("message", (event) => {
  const greeting = event.data;
  console.log(`<<< ${greeting}`);
  alert(greeting);
});


socket.addEventListener("error", (event) => {
  console.error("WebSocket encountered an error:", event);
});

socket.addEventListener("close", (event) => {
  console.log("WebSocket connection closed:", event);
});
