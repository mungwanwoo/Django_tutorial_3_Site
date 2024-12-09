// subscription.js
document.addEventListener('DOMContentLoaded', function() {
    // 필요한 DOM 요소들을 가져옵니다
    const likeButton = document.getElementById('likeButton');
    const likeCount = document.getElementById('likerCount');

    if (likeButton) {
        likeButton.addEventListener('click', function() {
            // 버튼 데이터에서 게시물 ID를 가져옵니다
            const postId = this.dataset.postId;
            // CSRF 토큰을 가져옵니다
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            // 중복 클릭 방지를 위해 버튼을 비활성화합니다
            this.disabled = true;

            // axios 설정
            axios.defaults.xsrfHeaderName = 'X-CSRFToken';
            axios.defaults.xsrfCookieName = 'csrftoken';

            // 서버에 구독 요청을 보냅니다
            axios.post(`/imageapp/image/${postId}/like/`, {}, {
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                const data = response.data;

                // 응답 데이터에 따라 UI를 업데이트합니다
                if (data.status === 'liked') {
                    likeButton.innerHTML = '<i class="bi bi-shield-fill-check"></i> 좋아요 취소하기';
                } else {
                    likeButton.innerHTML = '<i class="bi bi-shield"></i> 좋아요';
                }

                // 구독자 수를 업데이트합니다
                likeCount.textContent = `좋아요수: ${data.liker_count}명`;

                // 사용자에게 결과를 알립니다
                // alert(data.message);
            })
            .catch(error => {
                console.error('Error:', error);
                // alert('오류가 발생했습니다. 다시 시도해주세요.');
            })
            .finally(() => {
                // 작업이 완료되면 버튼을 다시 활성화합니다
                likeButton.disabled = false;
            });
        });
    }
});
