import styled from "@emotion/styled";
import LoginContainer from "../containers/LoginContainer";

const Button = styled.button`
  padding: 32px;
  font-size: 24px;
  border-radius: 4px;
  color: black;
  font-weight: bold;
  &:hover {
    color: white;
  }
`;

export default function Home() {
  return (
    <>
      <LoginContainer />
    </>
  );
}
