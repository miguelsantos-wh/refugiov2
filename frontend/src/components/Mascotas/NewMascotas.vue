<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>Nuevo Mascota</h2>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <div class="card">
          <div class="card-body">
            <form @submit="onSubmit">
              <div class="form-group row">
                <label for="nombre" class="col-sm-2 col-form-label">Nombre</label>
                <div class="col-sm-6">
                  <input type="text" placeholder="Nombre" name="nombre" class="form-control" v-model.trim="form.nombre">
                  <div class="error-message" v-if="errors.nombre">{{ errors.nombre[0] }}</div>
                </div>
              </div>
              <div class="form-group row">
                <label for="sexo" class="col-sm-2 col-form-label">Sexo</label>
                <div class="col-sm-6">
                  <input type="text" placeholder="Sexo" name="sexo" class="form-control" v-model.trim="form.sexo">
                  <div class="error-message" v-if="errors.sexo">{{ errors.sexo[0] }}</div>
                </div>
              </div>
              <div class="form-group row">
                <label for="edad_aproximada" class="col-sm-2 col-form-label">Edad aproximada</label>
                <div class="col-sm-6">
                  <input type="number" placeholder="Edad aproximada" name="edad_aproximada" class="form-control"
                  v-model.trim="form.edad_aproximada">
                  <div class="error-message" v-if="errors.edad_aproximada">{{ errors.edad_aproximada[0] }}</div>
                </div>
              </div>
              <div class="form-group row">
                <label for="fecha_rescate" class="col-sm-2 col-form-label">Fecha de rescate</label>
                <div class="col-sm-6">
                  <input type="date" placeholder="Fecha de rescate" name="fecha_rescate" class="form-control"
                  v-model.trim="form.fecha_rescate">
                  <div class="error-message" v-if="errors.fecha_rescate">{{ errors.fecha_rescate[0] }}</div>
                </div>
              </div>

              <div class="form-group row">
                <label for="persona" class="col-sm-2 col-form-label">Persona</label>
                <div class="col-sm-6">
                  <select type="persona" placeholder="Persona" name="persona" class="form-control"
                          v-model.trim="form.persona">
<!--                    <option value="Seleccionar persona">Seleccionar persona</option>-->
                    <option v-for="persona in form.personas" :key="persona.id" :value="persona.id">{{ persona.nombre }} {{ persona.apellidos }}</option>
                  </select>
                  <div class="error-message" v-if="errors.persona">{{ errors.persona[0] }}</div>
                </div>
              </div>

              <div class="form-group row">
                <label class="col-sm-2 col-form-label">Vacunas</label>
                <div class="col-sm-6">
                  <div v-for="vacuna in form.vacunas_total" :key="vacuna.id">
                    <label>
                      <input type="checkbox" :value="vacuna.id" v-model="form.vacuna">
                      {{ vacuna.nombre }}
                    </label>
                  </div>
                </div>
              </div>
              <div class="rows">
                <div class="col text-left">
                  <b-button type="submit" variant="primary">Guardar</b-button>
                  <b-button type="submit" class="btn-large-space" :to="{name: 'ListMascotas'}">Cancelar</b-button>
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
      form:{
        nombre: '',
        sexo: '',
        edad_aproximada: '',
        fecha_rescate: '',
        persona: '',
        personas: '',
        vacuna: [],
        vacunas_total: ''
      },
      errors: {}
    }
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault()
      const base_env = process.env.BASE_URI
      const base_hard = 'http://mascotasjose.net:8002/api/v2/'
      const path = base_env ? `${base_env}mascotas/` : `${base_hard}mascotas/`;

      axios.post(path, this.form).then((response) => {
        swal("Mascota agregada correctamente", "", "success")
          .then(() => {
            console.log(response.data);
            // location.href = "/mascotas";
            // this.$router.push("/mascotas");
            this.$router.push({ name: 'ListMascotas' });

          });
      }).catch((error) => {
        swal(`Mascota no agregada`, "", "error")
        if (error.response && error.response.data) {
          this.errors = error.response.data;
          console.log(this.errors)
        }
      })
    },

    getPersonas() {
      const base_env = process.env.BASE_URI
      const base_hard = 'http://mascotasjose.net:8002/api/v2/'
      const path = base_env ? `${base_env}personas/` : `${base_hard}personas/`;
      axios.get(path).then((response) => {
        this.form.personas = response.data
        console.log(this.form.personas)
      }).catch((error) => {
        console.log(error)
      })
    },

    getVacunas() {
      const base_env = process.env.BASE_URI
      const base_hard = 'http://mascotasjose.net:8002/api/v2/'
      const path = base_env ? `${base_env}vacunas/` : `${base_hard}vacunas/`;
      axios.get(path).then((response) => {
        this.form.vacunas_total = response.data
        console.log(this.form.vacunas_total)
      }).catch((error) => {
        console.log(error)
      })
    },
  },
  created() {
    this.getVacunas()
    this.getPersonas()
  }
}
</script>

<style scoped>

</style>
