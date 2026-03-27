document.addEventListener('DOMContentLoaded', function() {
    // 全ての完了切り替えフォームを取得
    const completeForms = document.querySelectorAll('.complete-form');
    
    completeForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault(); // フォームのデフォルト送信（リロード）を停止
            
            const itemDiv = form.closest('.todo-item');
            const incompleteColumn = document.querySelector('.incomplete-column');
            const completeColumn = document.querySelector('.complete-column');
            
            const url = form.action;
            // CSRFトークンを取得
            const token = document.querySelector('[name=csrfmiddlewaretoken]').value; 
            
            fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': token,
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'deleted_and_moved') {
                    
                    // 1. アニメーション実行 (縮小と不透明度低下)
                    itemDiv.style.transition = 'transform 0.5s ease-out, opacity 0.5s ease-out';
                    itemDiv.style.transform = 'scale(0.9)'; 
                    itemDiv.style.opacity = '0'; 
                    
                    // 2. アニメーション終了後にDOMを操作
                    setTimeout(() => {
                        // 新しい完了済みタスクのHTML要素を作成
                        const completedHtml = `
                            <div class="todo-item completed" id="todo-${data.pk}">
                                <div class="todo-details">
                                    <h3>${data.title}</h3>
                                    <small>完了日: ${data.created_at}</small>
                                </div>
                                <div class="actions">
                                    <form method="POST" action="/todos/${data.pk}/delete/" class="inline-form delete-form">
                                        <input type="hidden" name="csrfmiddlewaretoken" value="${token}"> 
                                        <button type="submit" class="delete-btn">削除</button>
                                    </form>
                                </div>
                            </div>
                        `;
                        
                        // 元の要素を未完了カラムから削除
                        itemDiv.remove();
                        
                        // 新しい要素を完了カラムに追加
                        completeColumn.querySelector('h2').insertAdjacentHTML('afterend', completedHtml);
                        
                        // 追加された要素に移動アニメーション（フェードイン）を適用
                        const newCompletedItem = document.getElementById(`todo-${data.pk}`);
                        newCompletedItem.style.transition = 'opacity 0.5s ease-in';
                        newCompletedItem.style.opacity = '0';
                        setTimeout(() => {
                            newCompletedItem.style.opacity = '1';
                        }, 50);

                    }, 500); // CSS transitionの時間(0.5s)と合わせる
                    
                } else if (data.status === 'error') {
                    alert(data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('タスクの完了処理中にエラーが発生しました。');
            });
        });
    });
});