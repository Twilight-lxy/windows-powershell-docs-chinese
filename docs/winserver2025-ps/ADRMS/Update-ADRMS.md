---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Configuration.dll-Help.xml
Module Name: ADRMS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrms/update-adrms?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-ADRMS
---

# 更新 ADRMS

## 摘要
更新现有的 AD RMS 服务器部署。

## 语法

```
Update-ADRMS [-ServiceAccount] <PSCredential> [[-PrivateKeyPassword] <SecureString>] [[-NewCspName] <String>]
 [-UpdateCryptographicModeOnly] [-Credential <PSCredential>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Update-ADRMS` cmdlet 用于更新已升级到该版本 Windows 的服务器上的 Active Directory 权限管理服务（AD RMS）服务器角色。此外，该 cmdlet 还可用于更改服务器上的 AD RMS 加密模式。

## 示例

### 示例 1：升级 AD RMS 服务器
```
PS C:\> $mySecureStringPassword = ConvertTo-SecureString -String <password> -AsPlainText -Force
PS C:\> $myCred = Get-Credential
PS C:\> Update-ADRMS -PrivateKeyPassword $mySecureStringPassword -ServiceAccount $myCred
```

这个示例用于升级一台使用集群密钥密码的 AD RMS 服务器和集群。该密码必须以安全的方式作为控制台输入进行指定。`Get-Credential` cmdlet 会弹出一个对话框，用于输入 AD RMS 服务账户的凭据（用户名和密码），这些凭据也是升级 AD RMS 所必需的。

### 示例 2：将 AD RMS 服务器升级到加密模式 2
```
PS C:\> $myCred = Get-Credential
PS C:\> Update-ADRMS -UpdateCryptographicModeOnly -ServiceAccount $myCred
```

这个示例用于将使用集群密钥密码的 AD RMS 服务器更新为加密模式 2。**Get-Credential** 命令会弹出一个对话框，要求用户输入进行此更新所需的 AD RMS 服务账户凭据（用户名和密码）。虽然不需要提供集群密钥密码，但如果服务器使用了 CSP 密钥存储机制，则必须指定 *NewCspName* 参数。

## 参数

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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

### -Credential
指定用于更新过程的用户凭据。如果指定了此参数，系统会提示您输入凭据。该参数的用法与“RunAs”命令类似。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
通过覆盖那些可能阻止命令成功的限制来强制完成该命令（只要所做的更改不会危及安全性）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewCspName
指定用于存储 AD RMS 服务器私钥的加密服务提供商（CSP）的新名称。此参数需与 *UpdateCryptographicMode* 参数结合使用，适用于那些使用 CSP 关键存储功能的 AD RMS 服务器。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PrivateKeyPassword
指定用于AD RMS集中管理密钥的密码。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ServiceAccount
指定用于 AD RMS 服务账户的域帐户的身份信息。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UpdateCryptographicModeOnly
这表示只需更新服务器的加密模式。要更新 AD RMS 服务器的加密模式，必须使用具有该服务器上本地 AD RMS 企业管理员组成员资格的账户进行登录。如果 AD RMS 服务器使用的是 CSP 密钥存储方式，则还需要指定 *NewCspName* 参数。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### SwitchParameter

### 字符串

### PSCredential

### SecureString

## 输出

## 备注

## 相关链接

