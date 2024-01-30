function DeleteTask({ onDelete }) {
  return (
    <button onClick={onDelete} className="DeleteButton">
      Delete
    </button>
  );
}

export default DeleteTask;
