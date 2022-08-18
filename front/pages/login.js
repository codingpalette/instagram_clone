import React from "react";
import Button from "../components/base/Button";
import Card from "../components/base/Card";
import Input from "../components/base/Input";

const login = () => {
  return (
    <div className="max-w-4xl m-auto min-h-screen flex justify-center items-center">
      <div className="flex-1 w-6/12r">
        <div className="img">
          <img src="/images/insta_login_main.png" alt="" />
        </div>
      </div>
      <div className="flex-1 w-6/12 max-w-[350px] flex flex-col">
        <Card>
          <div className="input flex flex-col w-[175px] mb-3 mt-9">
            <img src="/images/insta_logo.png" alt="" />
          </div>
          <div className="w-full mb-2 mt-6">
            <Input
              placeholder="전화번호, 사용자 이름 또는 이메일"
              style={{
                padding: "9px 8px 7px",
                background: "rgba(var(--b3f,250,250,250),1)",
              }}
            ></Input>
          </div>
          <div className="w-full mb-2">
            <Input
              placeholder="비밀번호"
              style={{
                padding: "9px 8px 7px",
                background: "rgba(var(--b3f,250,250,250),1)",
              }}
            ></Input>
          </div>
          <div className="w-full">
            <Button>로그인</Button>
          </div>
          <div className="w-full flex items-center mt-2.5 mb-5 justify-between">
            <div className="w-28 h-px bg-gray-400"></div>
            <div className=" text-center text-sm font-bold text-gray-400">
              또는
            </div>
            <div className="w-28 h-px bg-gray-400"></div>
          </div>
        </Card>
        <Card round>dsffd</Card>
      </div>
    </div>
  );
};
export default login;
