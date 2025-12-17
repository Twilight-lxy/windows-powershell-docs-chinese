---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adauthenticationpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADAuthenticationPolicy
---

# 删除 ADAuthenticationPolicy

## 摘要
删除一个 Active Directory 域服务（AD DS）的身份验证策略对象。

## 语法

```
Remove-ADAuthenticationPolicy [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADAuthenticationPolicy> [-Server <String>] [<CommonParameters>]
```

## 描述
`Remove-ADAuthenticationPolicy` cmdlet 用于删除 Active Directory® 域服务中的身份验证策略。

`Identity` 参数用于指定要删除的 Active Directory 域服务（AD DS）身份验证策略。您可以通过该策略的 distinguished name、GUID 或名称来识别它。此外，您还可以使用 `Identity` 参数来指定一个包含身份验证策略对象的变量，或者利用管道操作符将身份验证策略对象传递给该参数。

## 示例

### 示例 1：通过指定名称来删除身份验证策略
```
PS C:\> Remove-ADAuthenticationPolicy -Identity AuthenticationPolicy01
```

此命令会删除由*Identity*参数指定的身份验证策略。

### 示例 2：移除多个身份验证策略
```
PS C:\> Get-ADAuthenticationPolicy -Filter 'Enforce -eq $false' | Remove-ADAuthenticationPolicy
```

这个命令使用了 `Get-ADAuthenticationPolicy` cmdlet 并搭配 `Filter` 参数，来获取所有未被强制执行的身份验证策略。随后，管道运算符（pipeline operator）将过滤后的结果传递给 `Remove-ADAuthenticationPolicy` cmdlet。

## 参数

### -AuthType
指定要使用的身份验证方法。此参数的可接受值为：

- Negotiate or 0
- Basic or 1

默认的认证方法是“Negotiate”（协商）。对于基本认证方法（Basic authentication），需要建立安全套接字层（SSL）连接。

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
在运行该cmdlet之前，会提示您进行确认。

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
指定一个具有执行该任务权限的用户账户。默认值为当前用户。可以输入一个用户名（例如 User01 或 Domain01\User01），或者输入一个 **PSCredential** 对象（例如由 **Get-Credential** cmdlet 生成的对象）。

默认情况下，该cmdlet会使用当前登录用户的凭据进行操作，除非它是从Active Directory域服务Windows PowerShell提供程序驱动器中运行的。如果在提供程序驱动器中运行该cmdlet，则将使用与该驱动器关联的账户作为默认凭据。

如果你指定的凭据没有执行该任务的权限，那么此cmdlet会返回一个错误。

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

### -Identity
用于指定一个 Active Directory 域服务（Active Directory Domain Services）身份验证策略对象。请按照以下格式之一来指定该身份验证策略对象：

- A distinguished name
- GUID
- Name

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

The cmdlet searches the default naming context or partition to find the object.
If the cmdlet finds two or more objects, the cmdlet returns a non-terminating error.

```yaml
Type: ADAuthenticationPolicy
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Server
Specifies the Active Directory Domain Services instance to which to connect, by providing one of the following values for a corresponding domain name or directory server.
The service may be any of the following:  Active Directory Lightweight Domain Services, Active Directory Domain Services or Active Directory snapshot instance.

Specify the Active Directory Domain Services instance in one of the following ways:

Domain name values:

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

The default value for this parameter is determined by one of the following methods in the order that they are listed:

- By using the *Server* value from objects passed through the pipeline
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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。不过实际上这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无或 Microsoft.ActiveDirectory.Management_ADAuthenticationPolicy
此cmdlet接受一个身份验证策略对象。

## 输出

### System.Object

## 备注

## 相关链接

[Get-ADAuthenticationPolicy](./Get-ADAuthenticationPolicy.md)

[New-ADAuthenticationPolicy](./New-ADAuthenticationPolicy.md)

[Set-ADAuthenticationPolicy](./Set-ADAuthenticationPolicy.md)

[Windows PowerShell 中的 AD DS 管理 cmdlet](./activedirectory.md)

