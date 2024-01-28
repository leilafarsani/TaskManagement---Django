export async function fetchTasks() {
    try {
      const response = await fetch('');
      if (!response.ok) {
        throw new Error('Failed to fetch tasks');
      }
      const data = await response.json();
      return data;
    } catch (error) {
      throw new Error(`Error fetching tasks: ${error.message}`);
    }
  }
  