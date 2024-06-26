"use client"

import {useRouter} from "next/navigation"
export default function Login() {
  const router = useRouter();
  router.replace('i/flow/login')
  return (
    <>
      loginpage!!!!

    </>
  );
}

// router.push vs router.replace
// 둘다 페이지 i/flow/login 이동, 하지만 push의 경우 뒤로가면 /login으로 가고, replace는 그 전으로 간다.
// push의 경우 login으로 가고 또 push하고 반복되겠지?

// example
// Home => i/flow/login (replace), Home => login => i/flow/login