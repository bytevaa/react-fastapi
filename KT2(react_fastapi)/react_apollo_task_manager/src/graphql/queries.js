import { gql } from '@apollo/client';

export const ALL_TASKS = gql`
  query AllTasks {
    allTasks {
      id
      title
      description
      isCompleted
      category { name color }
    }
  }
`;
