async function search() {
    let name = document.getElementById("input").value.toLowerCase();
    let response = await fetch(`https://pokeapi.co/api/v2/pokemon/${name}`);
  
    if (response.ok) {
      let data = await response.json();
  
      // Format and show some useful data
      const result = `
  Name: ${data.name}
  ID: ${data.id}
  Type: ${data.types.map(t => t.type.name).join(", ")}
  Height: ${data.height}
  Weight: ${data.weight}
  Abilities: ${data.abilities.map(a => a.ability.name).join(", ")}
      `;
  
      document.getElementById("result").textContent = result;
    } else {
      document.getElementById("result").textContent = "❌ Pokémon not found!";
    }
  }
  