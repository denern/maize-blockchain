import React from 'react';
import { SvgIcon, SvgIconProps } from '@material-ui/core';
import { ReactComponent as MaizeIcon } from './images/maize.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={MaizeIcon} viewBox="0 0 150 58" {...props} />;
}
