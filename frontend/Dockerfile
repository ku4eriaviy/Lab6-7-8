# Dockerfile (frontend)
FROM node:20

# Рабочая директория
WORKDIR /app

# Копируем package.json и lock-файлы
COPY package*.json ./
RUN rm -rf node_modules package-lock.json

# Устанавливаем зависимости
RUN npm i

# Копируем весь проект
COPY . .

# Открываем порт Vite (по умолчанию 5173)
EXPOSE 5173

# Запускаем режим разработки с горячей перезагрузкой
CMD ["npm", "run", "dev"]