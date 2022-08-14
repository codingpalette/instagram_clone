import React from "react";
import Button from "../components/base/Button";
import Input from "../components/base/Input";

const login = () => {
  return (
    <div className="max-w-4xl m-auto min-h-screen flex justify-center items-center">
      <div className="flex-1 w-6/12">
        <div className="img">
          <img src="/images/insta_login_main.png" alt="" />
        </div>
      </div>
      <div className="flex-1 w-6/12 max-w-[350px] flex flex-col">
        <div className="border flex flex-col">
          <div
            style={{ margin: "36px auto 12px" }}
            className="input flex flex-col w-[175px]"
          >
            <img src="/images/insta_logo.png" alt="" />
          </div>
          <div style={{ margin: "0 40px 8px" }}>
            <Input
              placeholder="전화번호, 사용자 이름 또는 이메일"
              style={{
                padding: "9px 8px 7px",
              }}
            ></Input>
          </div>
          <div style={{ margin: "0 40px 8px" }}>
            <Input
              placeholder="비밀번호"
              style={{
                padding: "9px 8px 7px",
              }}
            ></Input>
          </div>
          <div style={{ margin: "0 40px 8px" }}>
            <Button>로그인</Button>
          </div>
        </div>
      </div>
    </div>
  );
};
export default login;
