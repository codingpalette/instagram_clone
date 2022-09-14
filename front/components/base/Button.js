import React from "react";
import styled from "@emotion/styled";

const Button = ({
  children,
  color = "primary",
  type = "button",
  className,
  disabled,
}) => {
  return (
    <>
      <ButtonBox
        className={`${className} w-full my-2 py-1.5 px-2.5 border-solid text-white text-sm font-semibold rounded border-gray-300`}
        type={type}
        color={color}
        disabled={disabled}
        // style={{ backgroundColor: "rgba(0,149,246,.3)" }}
      >
        {children}
      </ButtonBox>
    </>
  );
};

const ButtonBox = styled.button`
  background-color: ${(props) =>
    props.color === "primary"
      ? "#0095f6"
      : props.color === "secondary"
      ? "red"
      : "#000"};

  opacity: ${(props) => (props.disabled ? "0.3" : "1")};
`;

export default Button;
