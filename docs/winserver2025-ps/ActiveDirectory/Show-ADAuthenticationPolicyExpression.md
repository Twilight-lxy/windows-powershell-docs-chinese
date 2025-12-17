---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/show-adauthenticationpolicyexpression?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Show-ADAuthenticationPolicyExpression
---

# Show-ADAuthenticationPolicyExpression

## 摘要
显示“编辑访问控制条件”窗口，用于更新或创建安全描述符定义语言（SDDL）所表示的安全描述符。

## 语法

### AllowedToAuthenticateFrom
```
Show-ADAuthenticationPolicyExpression [-WhatIf] [-Confirm] [-AllowedToAuthenticateFrom]
 [-AuthType <ADAuthType>] [-Credential <PSCredential>] [[-SDDL] <String>] [-Server <String>]
 [[-Title] <String>] [<CommonParameters>]
```

### AllowedTo AuthenticateTo
```
Show-ADAuthenticationPolicyExpression [-WhatIf] [-Confirm] [-AllowedToAuthenticateTo] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [[-SDDL] <String>] [-Server <String>] [[-Title] <String>] [<CommonParameters>]
```

## 描述
`Show-ADAuthenticationPolicyExpression` cmdlet 使用 “编辑访问控制条件”（Edit Access Control Conditions）窗口来创建或修改 SDDL 安全描述符。

## 示例

### 示例 1：从 `AllowedTo AuthenticateFrom` 设置中获取值，并将其存储到文件中
```
PS C:\> Show-ADAuthenticationPolicyExpression -AllowedToAuthenticateFrom > someFile.txt
PS C:\> New-ADAuthenticationPolicy -Name "TestAuthenticationPolicy" -UserAllowedToAuthenticateFrom (Get-Acl .\AuthSettings.txt).sddl
```

该命令通过打开“编辑访问控制条件”窗口来获取允许的认证来源（AllowedToAuthenticateFrom）信息，并将这些信息存储在一个名为AuthSettings.txt的文件中。之后，该文件会被用来将新的身份验证策略应用到已获取的访问控制列表（ACL）上。

### 示例 2：设置 UserAllowedToAuthenticateFrom 属性
```
PS C:\> New-ADAuthenticationPolicy -Name "testAuthenticationPolicy" -UserAllowedToAuthenticateFrom (Show-ADAuthenticationPolicyExpression -AllowedToAuthenticateFrom)
```

这个示例使用 `New-ADAuthenticationPolicy` cmdlet 来创建一个身份验证策略，然后通过指定 `Show-ADAuthenticationPolicyExpression` cmdlet 作为参数的值来设置 `UserAllowedToAuthenticateFrom` 属性。

## 参数

### -AllowedToAuthenticateFrom
表示对象的 `AllowedToAuthenticateFrom` 列表会显示在 “编辑访问控制条件”（Edit Access Control Conditions）窗口中。

```yaml
Type: SwitchParameter
Parameter Sets: AllowedToAuthenticateFrom
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowedToAuthenticateTo
表示对象的 **AllowedToAuthenticateTo** 列表会显示在 “编辑访问控制条件” 窗口中。

```yaml
Type: SwitchParameter
Parameter Sets: AllowedToAuthenticateTo
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AuthType
指定要使用的身份验证方法。该参数的可接受值为：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”。对于“Basic”身份验证方法来说，需要建立安全套接字层（SSL）连接。

```yaml
Type: ADAuthType
Parameter Sets: (All)
Aliases:
Accepted values: Negotiate, Basic

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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
指定一个具有执行该任务权限的用户账户。默认值为当前用户。可以输入用户名（例如 User01 或 Domain01\User01），或者输入一个 **PSCredential** 对象（例如通过 [Get-Credential](https://go.microsoft.com/fwlink/?LinkID=293936) cmdlet 生成的 credential）。

默认情况下，该cmdlet会使用当前登录用户的凭据进行操作，除非它是从Active Directory域服务Windows PowerShell提供程序驱动器中运行的。如果在Active Directory提供程序驱动器中运行该cmdlet，则默认使用与该驱动器关联的账户的凭据。

如果您指定的凭据没有执行该任务的权限，那么此 cmdlet 会返回一个错误。

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

### -SDDL
指定安全描述符的 SDDL（Security Description Language）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Server
用于指定要连接的 Active Directory 域服务实例，可通过提供相应的域名或目录服务器的值来实现。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- A fully qualified domain name
- A NetBIOS name

Directory server values:

- A fully qualified directory server name
- A NetBIOS name
- A fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

- By using the **Server** value from objects passed through the pipeline
- By using the server information associated with the Active Directory Domain Services Windows PowerShell provider drive, when the cmdlet runs in that drive
- By using the domain of the computer running Windows PowerShell

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Title
为SDDL安全描述符指定一个标题。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生的后果。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 `System.String`
此cmdlet接受一个SDDL安全描述符。

## 输出

### System.Object
此cmdlet输出一个SDDL安全描述符。

## 备注

## 相关链接

[New-ADAuthenticationPolicy](./New-ADAuthenticationPolicy.md)

[Windows PowerShell中的AD DS管理Cmdlet](./activedirectory.md)

