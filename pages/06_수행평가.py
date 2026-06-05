with tab2:
    st.subheader("📝 게이머 전용 30문항 블라인드 테스트")
    st.write("문항 순서와 정답 성향이 무작위로 완전히 뒤섞여 지표 예측이 불가능합니다. 내 진짜 게이밍 성향은 과연 무엇일까요?")
    st.caption("※ 모든 문항은 실제 MBTI 설문지처럼 가로형으로 깔끔하게 정렬되며, 초기에는 아무것도 선택되지 않습니다.")
    
    # 누적 스코어 딕셔너리
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    
    st.write("---")
    
    # 모든 문제를 다 풀었는지 체크하기 위한 리스트
    all_answered = True
    
    # 셔플된 게임 문항 순회 출력
    for display_idx, (original_idx, q_data) in enumerate(st.session_state.shuffled_questions):
        
        # 💡 [수정] 진짜 설문지처럼 보이도록 질문을 위에 굵게 표시
        st.markdown(f"**Q{display_idx+1}. {q_data['q']}**")
        
        # 💡 [수정] 가로로 나란히 정렬(horizontal=True)하고 기본 선택 해제(index=None)
        choice = st.radio(
            label=f"Q{display_idx+1}_label", 
            options=[q_data['a1'], q_data['a2']], 
            index=None,                      # 🔥 최초에 무조건 1번 선택되던 버그 수정! 아무것도 선택 안 됨
            horizontal=True,                 # 🔥 보기 편하게 양옆으로 배치되도록 수정!
            key=f"gamer_q_{original_idx}",
            label_visibility="collapsed"     # 불필요한 라디오 내부 제목 숨김
        )
        st.write("") # 문항 사이 깔끔한 여백 공백
        
        # 유저가 선택했다면 스코어에 반영, 안 했다면 변수를 False로 변경
        if choice:
            if choice == q_data['a1']:
                scores[q_data['val1']] += 1
            else:
                scores[q_data['val2']] += 1
        else:
            all_answered = False  # 하나라도 누락되면 False가 됨
            
    st.write("---")
    
    # 결과 계산 및 히든 노출 버튼
    if st.button("📊 나의 게이머 MBTI 결과 확인하기"):
        if not all_answered:
            st.warning("⚠️ 아직 풀지 않은 문제가 있습니다! 30개의 모든 질문에 답한 뒤 결과를 확인해 주세요.")
        else:
            res_ei = "E" if scores["E"] >= scores["I"] else "I"
            res_sn = "S" if scores["S"] >= scores["N"] else "N"
            res_tf = "T" if scores["T"] >= scores["F"] else "F"
            res_jp = "J" if scores["J"] >= scores["P"] else "P"
            
            final_result = res_ei + res_sn + res_tf + res_jp
            
            st.balloons()
            st.success(f"🎉 분석 완료! 당신의 숨겨진 게이머 MBTI는 **[{final_result}]** 입니다!")
            st.markdown(f"👉 **[{final_result}] 유형 특징:** *{mbti_descriptions[final_result]}*")
            
            st.markdown(f"<h4>🎮 [{final_result}] 유형에게 최적화된 추천 인생 게임</h4>", unsafe_allow_html=True)
            for g in mbti_games[final_result]:
                st.info(f"**{g['name']}** ({g['mode']})\n\n↳ {g['style']}")
                
            st.caption("💡 팁: 결과가 마음에 든다면 '게임 추천 및 찜하기' 탭으로 이동해서 위시리스트에 담보세요.")
