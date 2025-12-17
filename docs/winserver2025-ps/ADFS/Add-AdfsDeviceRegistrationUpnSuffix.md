---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfsdeviceregistrationupnsuffix?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsDeviceRegistrationUpnSuffix
---

# 为 AdFS 设备注册添加 UPN 后缀

## 摘要
添加一个自定义的 UPN 后缀。

## 语法

```
Add-AdfsDeviceRegistrationUpnSuffix [-UpnSuffix] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-AdfsDeviceRegistrationUpnSuffix` cmdlet 可以添加一个自定义的用户主体名称（UPN）后缀，该后缀在您使用 Active Directory Federation Services (AD FS) 注册设备时可以使用。

在许多环境中，当 Active Directory Federation Services (AD FS) 的部署完成后，会为用户添加额外的 UPN 后缀。运行此 cmdlet 可以支持使用新 UPN 后缀的用户进行设备注册。该 cmdlet 会配置一个与相应 UPN 后缀匹配的 Secure Sockets Layer (SSL) 绑定。UPN 后缀必须在 AD FS 的 SSL 证书中拥有对应的注册名称（例如 `enterpriseregistration.upn`）。您也可以使用通配符 SSL 证书来覆盖所有可能的注册名称。

## 示例

### 示例 1：为注册设备添加 UPN 后缀
```
PS C:\> Add-AdfsDeviceRegistrationUpnSuffix -UpnSuffix "Northamerica.Contoso.com"
```

此命令会在设备注册服务初始部署后，将“UPN”后缀“Northamerica.Contoso.com”添加到AD FS响应的设备注册请求所使用的后缀列表中。

## 参数

### -UpnSuffix
用于指定一个 UPN 后缀。该 cmdlet 会添加并配置您指定的 UPN 后缀，并将其视为有效的注册用 UPN 后缀。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您确认是否要继续操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上，该cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

字符串对象通过*UpnSuffix*参数被接收。

## 输出

## 备注

## 相关链接

[Get-AdfsDeviceRegistrationUpnSuffix](./Get-AdfsDeviceRegistrationUpnSuffix.md)

[Remove-AdfsDeviceRegistrationUpnSuffix](./Remove-AdfsDeviceRegistrationUpnSuffix.md)

[Set-AdfsDeviceRegistrationUpnSuffix](./Set-AdfsDeviceRegistrationUpnSuffix.md)

