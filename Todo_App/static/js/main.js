const { createApp, onMounted } = Vue; 
createApp({
    setup() {
        onMounted(() => {
            const circles = document.querySelectorAll('.circle');
            
            const colors = [
                'rgba(255, 255, 255, 0.3)', 'rgba(255, 250, 250, 0.3)',
                'rgba(255, 245, 247, 0.3)', 'rgba(255, 240, 245, 0.3)',
                'rgba(255, 228, 235, 0.3)', 'rgba(255, 209, 220, 0.3)',
                'rgba(255, 192, 203, 0.3)', 'rgba(255, 182, 193, 0.3)',
                'rgba(255, 174, 185, 0.3)', 'rgba(255, 160, 180, 0.3)',
                'rgba(255, 145, 175, 0.3)', 'rgba(255, 130, 170, 0.3)',
                'rgba(255, 105, 180, 0.3)', 'rgba(255, 110, 150, 0.3)',
                'rgba(255, 120, 160, 0.3)', 'rgba(240, 128, 128, 0.3)'
            ];

            circles.forEach((circle) => {
                const inner = circle.querySelector('.circle-inner');
                if (!inner) return;

                //サイズと位置の設定
                const sizeValue = Math.floor(Math.random() * 120 + 50);
                circle.style.width = `${sizeValue}px`;
                circle.style.height = `${sizeValue}px`;
                circle.style.left = `${Math.floor(Math.random() * 100)}%`;
                
                // 上昇アニメーションの設定
                const upDuration = Math.random() * 10 + 15;
                circle.style.animationDuration = `${upDuration}s`;
                circle.style.animationDelay = `${Math.random() * upDuration * -1}s`;

                //  回転アニメーションの設定
                const rotateDuration = Math.random() * 5 + 5;
                inner.style.animationDuration = `${rotateDuration}s`;
                inner.style.animationDelay = `${Math.random() * rotateDuration * -1}s`;

                // 4. 色の設定
                inner.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            });
        });

    }
}).mount('#app');