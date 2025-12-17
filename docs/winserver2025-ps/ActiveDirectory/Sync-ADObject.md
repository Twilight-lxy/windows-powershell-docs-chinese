---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/sync-adobject?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Sync-ADObject
---

# 同步 AD 对象

## 摘要
在任意两个拥有相同分区的域控制器之间复制单个对象。

## 语法

```
Sync-ADObject [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Destination] <String>
 [-Object] <ADObject> [-PassThru] [-PasswordOnly] [[-Source] <String>] [<CommonParameters>]
```

## 描述
`Sync-ADObject` cmdlet 可以在任意两个具有相同分区结构的域控制器之间复制单个对象。这两个域控制器不一定是直接进行数据复制的伙伴关系。此外，您还可以使用此 cmdlet 将密码信息填充到只读域控制器（RODC）的缓存中。

## 示例

### 示例 1：将一个对象复制到另一个位置
```
PS C:\> Sync-ADObject -Object "CN=AccountManagers,OU=AccountDeptOU,DC=corp,DC=contoso,DC=com" -Source "corp-DC01" -Destination "corp-DC02"
```

此命令将一个具有以下区分名称的对象从 corp-DC01 复制到 corp-DC02：CN=AccountManagers, OU=AccountDeptOU, DC=corp, DC=contoso, DC=com。

### 示例 2：将密码预先缓存到域控制器中
```
PS C:\> Get-ADUser -Identity pattifuller | Sync-ADObject -Destination "corp-RODC01" -PasswordOnly
```

此命令使用用户的SAM账户名称，将Patti Fuller的密码预先缓存到只读域控制器corp-RODC01中。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值为：

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
指定一个具有执行此操作权限的用户账户。默认值为当前用户。

请输入一个用户名，例如 User01 或 Domain01\User01；或者输入一个 **PSCredential** 对象（该对象可以通过 [Get-Credential](https://go.microsoft.com/fwlink/?LinkID=293936) cmdlet 生成）。如果您输入了用户名，系统会提示您输入密码。

此参数不受任何随 Windows PowerShell 安装的提供程序的支持。

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

### -Destination
指定作为同步数据目的地的 Active Directory 服务器的身份。此参数的用法与在 **Set-ADObject** cmdlet 中使用的 **Server** 参数类似，但存在一些限制：不允许使用域名或森林名称。用于指定目标服务器的有效格式包括：

- Host name
- Host name and port
- Fully qualified directory server name and port
- IP address
- IP address and port

```yaml
Type: String
Parameter Sets: (All)
Aliases: Server, HostName, IPv4Address

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Object
Specifies an Active Directory object by providing one of the following property values.
The identifier in parentheses is the Lightweight Directory Access Protocol (LDAP) display name for the attribute.
The acceptable values for this parameter are:

- A distinguished name
- A GUID (objectGUID)

The cmdlet searches the default naming context or partition to find the object.
If two or more objects are found, the cmdlet returns a non-terminating error.

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

Derived types, such as the following, are also accepted:

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADOrganizationalUnit**
- **Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy**
- **Microsoft.ActiveDirectory.Management.ADDomain**

```yaml
Type: ADObject
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru
Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

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

### -PasswordOnly
Indicates that this cmdlet populates a read-only domain controller (RODC) password cache with the password of the account specified in the **Object** parameter.
If specified, no data other than the password is replicated.

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

### -Source
Specifies the identity of the Active Directory server that acts as the source for synchronizing this data.
This parameter works similarly to the **Server** parameter as used on the **Set-ADObject** cmdlet with some restrictions.
You cannot use domain or forest names.

Valid formats for specifying the destination server are the following:

- Host name
- Host name and port
- Fully qualified directory server name and port
- IP address
- IP address and port

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

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### Microsoft.ActiveDirectory.Management.ADObject
Derived types, such as the following are also accepted:

- **Microsoft.ActiveDirectory.Management.ADGroup**
- **Microsoft.ActiveDirectory.Management.ADUser**
- **Microsoft.ActiveDirectory.Management.ADComputer**
- **Microsoft.ActiveDirectory.Management.ADServiceAccount**
- **Microsoft.ActiveDirectory.Management.ADOrganizationalUnit**
- **Microsoft.ActiveDirectory.Management.ADFineGrainedPasswordPolicy**
- **Microsoft.ActiveDirectory.Management.ADDomain**

## 输出

## 备注

## 相关链接

[Get-ADObject](./Get-ADObject.md)

[Move-ADObject](./Move-ADObject.md)

[New-ADObject](./New-ADObject.md)

[Remove-ADObject](./Remove-ADObject.md)

[重命名 AD 对象](./Rename-ADObject.md)

[恢复 AD 对象](./Restore-ADObject.md)

[Set-ADObject](./Set-ADObject.md)

