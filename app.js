
function getClients() {
    fetch('/api/clients') // Отправьте GET-запрос на адрес /api/clients
        .then(response => response.json()) // Обработайте ответ в формате JSON
        .then(data => {
            
        })
        .catch(error => {
            // Обработайте ошибку, если произошла ошибка при получении данных
            console.error('Ошибка получения списка клиентов:', error);
        });
}

// Вызовите функцию для получения списка клиентов при загрузке страницы
document.addEventListener('DOMContentLoaded', getClients);
