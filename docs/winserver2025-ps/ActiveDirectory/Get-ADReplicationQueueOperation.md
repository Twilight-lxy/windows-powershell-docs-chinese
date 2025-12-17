---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adreplicationqueueoperation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADReplicationQueueOperation
---

# Get-ADReplicationQueueOperation

## 摘要
返回指定服务器的复制队列中的内容。

## 语法

```
Get-ADReplicationQueueOperation [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Server] <String>
 [-Filter <String>] [[-Partition] <String[]>] [<CommonParameters>]
```

## 描述
`Get-ADReplicationQueueOperation` cmdlet 可以返回复制队列中所有待处理的操作。在复制操作处于待处理状态时，该 cmdlet 可用于查看这些操作的状态。

你可以通过脚本调用 **Get-ADReplicationQueueOperation** cmdlet 来观察操作在复制过程中何时被移出队列。此外，该 cmdlet 还允许根据 **ADReplicationOperation** 对象的任何属性进行筛选。

复制队列的工作原理如下：假设一个域控制器有五个入站复制连接。当该域控制器根据预设的时间表或接收到的通知生成更改请求时，它会为每个请求添加一个工作项到待同步请求队列的末尾。每个待同步请求都对应一对“源域控制器”和“目录分区”，例如：从DC1同步架构目录分区，或者删除ApplicationX目录分区。

当一个工作项被加入到复制队列中时，通知机制和轮询间隔就不再适用了。相反，域控制器会在该工作项到达复制队列的头部时立即开始处理它（即从源域控制器那里同步数据）。这个过程会一直持续，直到目标域控制器与源域控制器完全同步，或者出现错误，又或者是由于有更高优先级的操作而使得同步进程被中断。

## 示例

### 示例 1：获取复制队列中待处理的操作
```
PS C:\> Get-ADReplicationQueueOperation -Server "corp-DC01.corp.contoso.com"
```

此命令用于获取域控制器 corp-DC01 的复制队列中尚未完成的操作。该域控制器的标识是通过其完全限定域名（FQDN）来指定的。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”。

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

请输入一个用户名，例如 User01 或 Domain01\User01；或者输入一个 **PSCredential** 对象（例如通过 **Get-Credential** cmdlet 生成的对象）。如果您输入了用户名，系统会提示您输入密码。

此参数不被任何与 Windows PowerShell 一起安装的提供程序支持。

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

### -Filter
该参数用于指定以提供者格式或语言表示的过滤器。其值用于限定“Path”参数的使用范围。过滤器的语法（包括通配符的使用方式）取决于具体的提供者。与其它参数相比，过滤器更为高效：因为提供者在检索对象时会直接应用这些过滤器，而不是等到对象被检索出来后再由 Windows PowerShell 进行过滤处理。

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

### -Partition
用于指定 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上支持的命名上下文之一。此 cmdlet 会在该分区中搜索由 *Identity* 参数所定义的对象。

在许多情况下，如果未指定“Partition”参数的值，系统会使用默认值。确定默认值的规则如下所示。请注意，列出的规则会按顺序依次进行评估；一旦确定了默认值，后续的规则将不再被执行。

在 Active Directory 域服务（AD DS）环境中，以下情况下会为“分区”（Partition）设置默认值：

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent (DSA) object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter does not take any default value.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: NC, NamingContext

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定要连接的 AD DS 实例，为此提供相应的域名或目录服务器之一。该服务可以是以下类型中的任意一种：AD LDS、AD DS 或 Active Directory 快照实例。

以下是指定 AD DS 实例的几种方式：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

- By using the *Server* value from objects passed through the pipeline
- By using the server information associated with the AD DS Windows PowerShell provider drive, when the cmdlet runs in that drive
- By using the domain of the computer running Windows PowerShell

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ActiveDirectory.Management ADDirectoryServer
一个类结构，用于表示一个或多个 Active Directory 服务器。

## 输出

### Microsoft.ActiveDirectory.Management.AdReplicationOperation
一个类结构，用于表示一个或多个 Active Directory 复制操作。

## 备注

## 相关链接

