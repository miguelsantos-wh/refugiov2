<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>Editar Mascota</h2>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <div class="card">
          <div class="card-body">
            <form>
              <div class="form-group row">
                <label for="nombre" class="col-sm-2 col-form-label">#</label>
                <div class="col-sm-6">
                  <input type="text" placeholder="Id" name="id" class="form-control" v-model.trim="form.id" disabled>
                </div>
              </div>
              <div class="form-group row">
                <label for="nombre" class="col-sm-2 col-form-label">Nombre Completo</label>
                <div class="col-sm-6">
                  <input type="text" placeholder="Nombre Completo" name="nombre" class="form-control"
                         v-model.trim="form.nombre_completo" disabled>
                </div>
              </div>
              <div class="form-group row">
                <label for="edad" class="col-sm-2 col-form-label">Edad</label>
                <div class="col-sm-6">
                  <input type="text" placeholder="Edad" name="edad" class="form-control"
                         v-model.trim="form.edad" disabled>
                </div>
              </div>
              <div class="form-group row">
                <label for="telefono" class="col-sm-2 col-form-label">Telefono</label>
                <div class="col-sm-6">
                  <input type="text" placeholder="Telefono" name="telefono" class="form-control"
                         v-model.trim="form.telefono" disabled>
                </div>
              </div>
              <div class="form-group row">
                <label for="email" class="col-sm-2 col-form-label">Email</label>
                <div class="col-sm-6">
                  <input type="text" placeholder="Email" name="email" class="form-control"
                         v-model.trim="form.email" disabled>
                </div>
              </div>
              <div class="form-group row">
                <label for="domicilio" class="col-sm-2 col-form-label">Domicilio</label>
                <div class="col-sm-6">
                  <input type="text" placeholder="Domicilio" name="domicilio" class="form-control"
                         v-model.trim="form.domicilio" disabled>
                </div>
              </div>
              <div class="rows">
                <div class="col text-left">
<!--                  <b-button type="submit" variant="primary">Editar</b-button>-->
                  <b-button type="submit" class="btn-large-space" :to="{name: 'ListMascotas'}">Regresar</b-button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import swal from "sweetalert";
export default {
  data() {
    return {
      mascotaId: this.$route.params.mascotaId,
      form:{
        id: '',
        nombre: '',
        apellidos: '',
        nombre_completo: '',
        edad: '',
        telefono: '',
        email: '',
        domicilio: ''
      }
    }
  },
  methods: {
    getPersona() {
      const base_env = process.env.BASE_URI
      const base_hard = 'http://mascotasjose.net:8002/api/v2/'
      const path = base_env ? `${base_env}mascotas/${this.mascotaId}/persona/` : `${base_hard}mascotas/${this.mascotaId}/persona/`;

      axios.get(path).then((response) => {
        this.form.id = response.data.id
        this.form.nombre = response.data.nombre
        this.form.apellidos = response.data.apellidos
        this.form.nombre_completo = response.data.nombre + " " + response.data.apellidos
        this.form.edad = response.data.edad
        this.form.telefono = response.data.telefono
        this.form.email = response.data.email
        this.form.domicilio = response.data.domicilio
        console.log(response.data)
      }).catch((error) => {
        console.log(error)
      })
    }
  },
  created() {
    this.getPersona()
  }
}
</script>

<style scoped>

</style>
