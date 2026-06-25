<template>

  <div class="container">

    <h1>
      🎓 Sistema Acadêmico UniVenturi
    </h1>

    <div class="cards">

      <div class="card">
        👨‍🎓
        <h2>Alunos</h2>
        <p>0</p>
      </div>

      <div class="card">
        📚
        <h2>Cursos</h2>
        <p>0</p>
      </div>

      <div class="card">
        📝
        <h2>Notas</h2>
        <p>0</p>
      </div>

      <div class="card">
        📈
        <h2>Média Geral</h2>
        <p>0</p>
      </div>

    </div>

  </div>

</template>

<style scoped>

.container{
  padding:30px;
}

.cards{
  display:flex;
  gap:20px;
  margin-top:30px;
}

.card{
  border:1px solid #ddd;
  border-radius:10px;
  padding:20px;
  width:180px;

  text-align:center;

  box-shadow:0 2px 5px rgba(0,0,0,.1);
}

</style>