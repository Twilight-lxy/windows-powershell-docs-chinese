---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adfinegrainedpasswordpolicysubject?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADFineGrainedPasswordPolicySubject
---

# 获取 AD 详细密码策略主题信息

## 摘要
获取应用了细粒度密码策略的用户和组。

## 语法

```
Get-ADFineGrainedPasswordPolicySubject [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADFineGrainedPasswordPolicy> [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-ADFineGrainedPasswordPolicySubject` cmdlet 可用于获取受细粒度密码策略约束的用户和组。

`Identity` 参数用于指定细粒度的密码策略。您可以通过其唯一名称、GUID 或名称来识别某个细粒度的密码策略。您也可以将 `Identity` 参数设置为某个细粒度密码策略对象变量（例如 `$<localPasswordPolicyObject>`），或者通过管道运算符将该细粒度密码策略对象传递给 `Identity` 参数。例如，您可以使用 `Get-ADFineGrainedPasswordPolicy` cmdlet 获取一个细粒度密码策略对象，然后通过管道运算符将其传递给 `Get-ADFineGrainedPasswordPolicySubject` cmdlet。

## 示例

### 示例 1：获取细粒度密码策略的主题（即该策略所针对的具体内容或目标）
```
PS C:\> Get-ADFineGrainedPasswordPolicySubject -Identity DomainUsersPSO | FT Name,ObjectClass,DistinguishedName -AutoSize
Name                     ObjectClass DistinguishedName
----                     ----------- -----------------
Domain Users group       CN=Domain   Users,CN=Users,DC=FABRIKAM,DC=COM
```

这个命令用于获取名为“DomainUsersPSO”的密码策略所关联的细粒度密码策略设置信息。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的认证方法是“Negotiate”。

基本身份验证方法需要使用安全套接字层（SSL）连接。

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

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该cmdlet是从Windows PowerShell提供程序的Active Directory模块驱动器中运行的。如果该cmdlet是从此类驱动器中运行的，则默认凭据将是与该驱动器关联的用户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01/User01），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行该任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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
通过提供以下属性值之一来指定一个 Active Directory 细粒度密码策略对象。括号中的标识符是该属性的轻型目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A name (name)

该 cmdlet 会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，该 cmdlet 会返回一个表示无法继续执行的错误（即非终止性错误）。

这个参数也可以通过管道获取该对象，或者你可以将此参数设置为细粒度密码策略对象的实例。

```yaml
Type: ADFineGrainedPasswordPolicy
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Server
指定要连接的 AD DS 实例，为此需提供以下值之一（对应于相应的域名或目录服务器）。该服务可以是以下类型中的任意一种：AD LDS、AD DS 或 Active Directory 快照实例。

以下列方式之一指定 AD DS 实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

- By using the *Server* value from objects passed through the pipeline
- By using the server information associated with the AD DS Windows PowerShell provider drive, when the cmdlet runs in that drive
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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft ActiveDirectory.Management.ADFineGrainedPasswordPolicy
一个细粒度的密码策略对象通过*Identity*参数被接收。

## 输出

### Microsoft.ActiveDirectory.Management.ADPrincipal
返回表示应用了细粒度密码策略的用户和组的主体对象（principal objects）。

## 备注
* This cmdlet does not work with AD LDS.
* This cmdlet does not work when targeting a snapshot using the *Server* parameter.

## 相关链接

[Add-ADFineGrainedPasswordPolicySubject](./Add-ADFineGrainedPasswordPolicySubject.md)

[Remove-ADFineGrainedPasswordPolicySubject](./Remove-ADFineGrainedPasswordPolicySubject.md)

