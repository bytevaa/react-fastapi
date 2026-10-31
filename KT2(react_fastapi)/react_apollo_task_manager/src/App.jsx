import { use, useState } from 'react';
import { useMutation, useQuery } from '@apollo/client';
import { ALL_TASKS } from './graphql/queries.js';
import { CREATE_TASK, COMPLETE_TASK, DELETE_TASK } from './graphql/mutations.js';


function TaskList() {
  const { loading, error, data } = useQuery(ALL_TASKS);
  const [completeTask, { error: mutationError }] = useMutation(COMPLETE_TASK, {
    refetchQueries: [{ query: ALL_TASKS }],
  });
  const [deleteTask, { error: deleteError }] = useMutation(DELETE_TASK, {
    refetchQueries: [{ query: ALL_TASKS }],
  })
  
  if (loading) return <p>Загрузка задач...</p>;
  if (error) return <p className="error">Не удалось загрузить задачи: {error.message}</p>;

  const tasks = data?.allTasks ?? [];
  return <section>
    <h2>Список задач</h2>
    {mutationError && <p className="error">Не удалось обновить задачу: {mutationError.message}</p>}
    {deleteError && <p className="error">Не удалось удалить задачу: {deleteError.message}</p>}

    {tasks.length === 0 && <p>Задач пока нет.</p>}
{tasks.map(task => (
  <article className="task" key={task.id}>
    <h3>{task.title}</h3>
    <p>{task.description}</p>
    <p>Категория: {task.category?.name ?? '-'} ({task.category?.color ?? '-'})</p>
    <p>Статус: {task.isCompleted ? 'Выполнена' : 'Не выполнена'}</p>
    
    {!task.isCompleted && (
      <button onClick={() => completeTask({ variables: { taskId: Number(task.id) } })}>
        Отметить выполненной
      </button>
    )}

    <button onClick={() => deleteTask({ variables: { taskId: Number(task.id) } }).catch(() => {})}>
      Удалить
    </button>
  </article>
))}
</section>

}

function CreateTaskForm() {
  const [title, setTitle] = useState('');
  const [createTask, { loading, error }] = useMutation(CREATE_TASK, {
    refetchQueries: [{ query: ALL_TASKS }],
    onCompleted: () => setTitle(''),
  });

  function handleSubmit(event) {
    event.preventDefault();
    const trimmedTitle = title.trim();
    if (!trimmedTitle) return;
    createTask({ variables: { title: trimmedTitle } }).catch(() => {});
  }

  return <section>
    <h2>Создать задачу</h2>
    <form onSubmit={handleSubmit}>
      <input value={title} onChange={event => setTitle(event.target.value)} placeholder="Название задачи" minLength={3} required />
      <button disabled={loading}>{loading ? 'Создание...' : 'Добавить'}</button>
    </form>
    {error && <p className="error">Не удалось создать задачу: {error.message}</p>}
  </section>;
}

export default function App() {
  return <main><h1>Менеджер задач</h1><CreateTaskForm /><TaskList /></main>;
}
