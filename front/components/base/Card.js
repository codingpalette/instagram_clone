import React from "react";

const Card = ({ children, round }) => {
  return (
    <>
      <div
        className={`border flex flex-col px-10 py-2.5 items-center  ${
          round ? "rounded-md" : ""
        }`}
      >
        {children}
      </div>
    </>
  );
};

export default Card;
