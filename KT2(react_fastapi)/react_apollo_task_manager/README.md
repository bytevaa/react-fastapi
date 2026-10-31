# React + Apollo Client

Требуется Node.js LTS. Установите зависимости командой `npm install`, затем запустите `npm run dev`.

React: http://localhost:5173
GraphQL endpoint в `src/main.jsx`: `http://localhost:8000/graphql`.

ВАЖНО: имена полей и аргументов в `src/graphql/queries.js` и `src/graphql/mutations.js` должны совпадать со Strawberry-схемой из темы 2.2. В шаблоне используются `allTasks`, `createTask(title:)`, `completeTask(taskId:)`, поля `isCompleted` и `taskId`. Если ваша схема использует snake_case или другие аргументы/типы, поправьте операции по фактической GraphQL-схеме. Для создания по этому минимальному заданию передаётся только title; если сервер требует description/category, нужно добавить их в форму и variables.
