import React from "react";
import Button from "../components/base/Button";
import Card from "../components/base/Card";
import Input from "../components/base/Input";
import Link from "next/link";
import { useForm } from "react-hook-form";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faAlignRight } from "@fortawesome/free-solid-svg-icons";
import { faGithub } from "@fortawesome/free-brands-svg-icons";

const Login = () => {
  const {register, handleSubmit, watch, formState: { errors },} = useForm();
  const onSubmit = (data) => {
    console.log(data);
  };
  return (
    <div className="max-w-4xl m-auto min-h-screen flex justify-center items-center">
      <div className=" pr-8  pb-3 w-6/12r">
        <div className="img">
          <img src="/images/insta_login_main.png" alt="" />
        </div>
      </div>

      <form
        onSubmit={handleSubmit(onSubmit)}
        className="flex-1 w-6/12 max-w-[350px] flex flex-col gap-2.5"
      >
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
              register={{...register("email", { required: true })}}
            ></Input>
            {errors.email && <span>This field is required</span>}
          </div>
          <div className="w-full mb-2">
            <Input
              placeholder="비밀번호"
              type="password"
              style={{
                padding: "9px 8px 7px",
                background: "rgba(var(--b3f,250,250,250),1)",
              }}
            ></Input>
          </div>
          <div className="w-full">
            <Button type="submit">로그인</Button>
          </div>
          <div className="w-full flex items-center mt-2.5 mb-5 justify-between">
            <div
              className="grow h-px"
              style={{ backgroundColor: "rgba(var(--b38,219,219,219),1)" }}
            ></div>
            <div
              style={{
                color: "#8e8e8e",
                fontSize: "13px",
                margin: "0 18px",
              }}
              className="grow-0 text-center font-semibold"
            >
              또는
            </div>
            <div
              style={{ backgroundColor: "rgba(var(--b38,219,219,219),1)" }}
              className="grow h-px"
            ></div>
          </div>
          <div className="text-sm w-full font-semibold text-center">
            <button style={{ color: "#000000d9" }}>카카오톡으로 로그인</button>
          </div>
          <div style={{ color: "#00376B" }} className="text-xs mt-3 mb-3">
            <Link href="/">비밀번호를 잊으셨나요?</Link>
          </div>
        </Card>
        <Card>
          <div className="text-sm py-4">
            <span>계정이 없으신가요? </span>
            <Link href="/">
              <a className="font-semibold" style={{ color: "#0095f6" }}>
                가입하기
              </a>
            </Link>
          </div>
        </Card>
        <div className="git">
          <div className="text-sm text-gray-700 text-center my-2.5">
            깃허브에 방문해보세요.
          </div>
          <div className="git_link flex gap-4 items-center justify-center pt-2.5">
            <a
              className="w-6/12 flex justify-center py-2 border rounded"
              href="https://github.com/codingpalette"
            >
              <div className="lee flex items-center">
                <FontAwesomeIcon icon={faGithub} size="lg" />
                <div className="flex ml-2.5 flex-col text-xs ">
                  <span>GitHub</span>
                  <span>codingpalette</span>
                </div>
              </div>
            </a>
            <a
              className="w-6/12 flex justify-center py-2 border rounded"
              href="https://github.com/c-ummer"
            >
              <div className="cho flex items-center">
                <FontAwesomeIcon icon={faGithub} size="lg" />
                <div className="flex ml-2.5 flex-col text-xs ">
                  <span>GitHub</span>
                  <span>c-ummer</span>
                </div>
              </div>
            </a>
          </div>
        </div>
      </form>
    </div>
  );
};
export default Login;