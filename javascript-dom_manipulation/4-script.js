document.querySelector('#add_item').addEventListener('click', () => {
  const item = document.createElement('li');
  item.textContent = 'Item';
  document.querySelector('.my_list').appendChild(item);
});
