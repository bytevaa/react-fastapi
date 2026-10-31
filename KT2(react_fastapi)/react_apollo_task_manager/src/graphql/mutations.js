import { gql } from '@apollo/client';

export const CREATE_TASK = gql`
  mutation CreateTask($title: String!) {
    createTask(title: $title) { id title }
  }
`;

export const COMPLETE_TASK = gql`
  mutation CompleteTask($taskId: Int!) {
    completeTask(taskId: $taskId) { id isCompleted }
  }
`;

export const DELETE_TASK = gql`
  mutation DeleteTask($taskId: Int!) {
    deleteTask(taskId: $taskId) 
  }
`;
