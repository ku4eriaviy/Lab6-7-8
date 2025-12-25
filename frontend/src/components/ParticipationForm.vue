<template>
  <div class="modal-overlay" @click="$emit('close')">
    <div class="modal" @click.stop>
      <h2>Заявка на участие</h2>
      <form @submit.prevent="submit">
        <label>
          Комментарий (необязательно):
          <textarea v-model="comment" rows="4"></textarea>
        </label>

        <div class="buttons">
          <button type="button" @click="$emit('close')" class="btn btn-secondary">Отмена</button>
          <button type="submit" class="btn btn-primary">Отправить</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { defineProps, defineEmits } from 'vue'

const props = defineProps({
  eventId: [String, Number]
})

const emit = defineEmits(['close', 'submitted'])

const comment = ref('')

const submit = async () => {
  try {
    await axios.post(`/api/events/${props.eventId}/participate/`, { comment: comment.value })
    emit('submitted')
    emit('close')
  } catch (err) {
    alert('Ошибка при отправке заявки')
    console.error(err)
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal {
  background: white;
  padding: 32px;
  border-radius: 12px;
  width: 100%;
  max-width: 500px;
}

.modal h2 {
  margin-bottom: 24px;
}

label {
  display: block;
  margin-bottom: 16px;
}

textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  resize: vertical;
}

.buttons {
  margin-top: 24px;
  display: flex;
  gap: 16px;
  justify-content: flex-end;
}
</style>