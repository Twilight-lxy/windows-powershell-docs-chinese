---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/test-adserviceaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-ADServiceAccount
---

# 测试 ADServiceAccount

## 摘要
从计算机上测试一个托管服务账户。

## 语法

```
Test-ADServiceAccount [-AuthType <ADAuthType>] [-Identity] <ADServiceAccount> [<CommonParameters>]
```

## 描述
`Test-ADServiceAccount` cmdlet 用于从本地计算机测试托管服务账户（Managed Service Account，简称 MSA）。

`Identity` 参数用于指定要测试的 Active Directory MSA（Microsoft Services Account）账户。您可以通过该账户的唯一名称（DN）、GUID、安全标识符（SID）或 Security Account Manager (SAM) 账户名来识别它。您也可以将此参数设置为某个 MSA 对象变量（例如 `$<localMSA>`），或者通过管道将该 MSA 对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADServiceAccount` 命令获取一个 MSA 对象，然后将该对象通过管道传递给 `Test-ADServiceAccount` cmdlet 进行测试。

## 示例

### 示例 1：测试多源聚合服务（MSA）
```
PS C:\> Test-ADServiceAccount -Identity MSA1
True
```

此命令从本地计算机测试指定的服务账户（MSA1）。测试结果会表明该账户是否可以使用，即该账户是否可以通过当前的凭据进行身份验证，并且能否访问相应的域名。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”。

基本认证方法需要使用安全套接字层（SSL）连接。

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

### -Identity
通过提供以下属性值之一来指定一个由 Active Directory 管理的服务账户对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

该 cmdlet 会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该 cmdlet 会返回一个非终止性的错误（即无法正常完成操作）。

这个参数也可以通过管道来获取该对象，或者你可以将该参数设置为一个对象实例。

```yaml
Type: ADServiceAccount
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft.ActiveDirectory.Management.ADServiceAccount
一个托管服务账户对象通过“*Identity*”参数被接收。

## 输出

### 无

## 备注

## 相关链接

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

[安装 AD 服务账户](./Install-ADServiceAccount.md)

[New-ADServiceAccount](./New-ADServiceAccount.md)

[Remove-ADServiceAccount](./Remove-ADServiceAccount.md)

[Set-ADServiceAccount](./Set-ADServiceAccount.md)

[卸载 ADServiceAccount](./Uninstall-ADServiceAccount.md)

