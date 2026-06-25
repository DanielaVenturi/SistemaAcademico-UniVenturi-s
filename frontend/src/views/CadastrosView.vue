<template>

  <div class="container">

    <h1>📝 Cadastros</h1>

    <div class="cards">

      <div class="card">

        <h2>
          👨‍🎓 Alunos
        </h2>

        <p>
          Cadastro de estudantes
        </p>

        <button>
          Novo Aluno
        </button>

      </div>

      <div class="card">

        <h2>
          📚 Cursos
        </h2>

        <p>
          Cadastro de cursos
        </p>

        <button>
          Novo Curso
        </button>

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
}

.card{
  border:1px solid #ddd;
  padding:20px;
  width:250px;
  border-radius:10px;
}

button{
  padding:10px;
}

</style>