import { defineStore } from 'pinia';
import { computed, ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

// const PROXY = window.location.hostname === 'localhost' ? '' : '/proxy';
// const URL = `${PROXY}`;
const baseUrl = '/api/user/';

export const userInfoStore = defineStore('userInfo', () => {
  const userInfo = ref({ "age": 0, "sex": "", "personality": 0 , "price_type":1 , "category_1":""});
  const matchedItems = ref([]);
  const amazonMatchedItems = ref([]);
  const router = useRouter();

  function addUserInfo(payload){
    const { key, value } = payload;
    userInfo.value[key] = value
  }
  
  async function postData(data) {
    try {
      const response = await axios.post(baseUrl, data);
      console.log("성공", response);

      // 여기서 반환된 데이터를 처리할 수 있습니다.
      userInfo.value['user_id'] = response.data.user_id;
      console.log("유저 리스폰스",userInfo.value['user_id']);
    } catch (error) {
      console.error('Error posting data:', error);
    }
  }

  async function getData() {
    try {
      console.log("실행");
      const response = await axios.get(`${baseUrl}matched-items/${userInfo.value['user_id']}`);
      console.log("성공", response.data);

      // 여기서 반환된 데이터를 리스트에 저장합니다.
      matchedItems.value = response.data;
    } catch (error) {
      console.error('Error posting data:', error);
    }
  }

  function routeTo(path){
    router.push(path);
  }

  const getDataAll = computed(() => userInfo.value);

  return {userInfo, addUserInfo, routeTo, postData, getData, getDataAll, matchedItems, amazonMatchedItems}
},{persist:true});



