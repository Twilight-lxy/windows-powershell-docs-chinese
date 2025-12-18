---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsrmembership?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsrMembership
---

# Get-DfsrMembership

## 摘要
获取复制组成员的会员设置信息。

## 语法

```
Get-DfsrMembership [[-GroupName] <String[]>] [[-ComputerName] <String[]>] [[-DomainName] <String>]
 [<CommonParameters>]
```

## 描述
`Get-DfsrMembership` cmdlet 可以获取复制组成员的成员资格设置。复制组的成员会托管被复制的文件夹。可以使用 `Add-DfsrMember` cmdlet 将某个成员添加到组中；添加成员时会创建一个包含默认值的成员资格记录。你可以使用当前的 `Get-DfsrMembership` cmdlet 来查看成员资格的设置，同时也可以使用 `Set-DfsrMembership` cmdlet 来修改这些设置。

## 示例

### 示例 1：获取所有组的所有成员
```
PS C:\> Get-DfsrMembership -GroupName * -ComputerName *
GroupName                   : RG01
ComputerName                : SRV01
FolderName                  : RF01
GroupDomainName             : corp.contoso.com
ComputerDomainName          : corp.contoso.com
Identifier                  : 9931c757-b252-4f04-8347-53575610c423
DistinguishedName           : CN=72c0c2bc-8a4e-4984-a23c-2efadc238724,CN=957751c2-15f0-429b-8688-44c22044226d,CN=DFSR-L
                              ocalSettings,CN=SRV01,OU=Domain Controllers,DC=corp,DC=contoso,DC=com
ContentPath                 : c:\rf01
PrimaryMember               : False
StagingPath                 : c:\rf01\DfsrPrivate\Staging
StagingPathQuotaInMB        : 4096
MinimumStagingFileSize      : Size256KB
ConflictAndDeletedPath      : c:\rf01\DfsrPrivate\ConflictAndDeleted
ConflictAndDeletedQuotaInMB : 660
ReadOnly                    : False
RemoveDeletedFiles          : False
Enabled                     : True
DfsnPath                    :
State                       : Normal

GroupName                   : RG01
ComputerName                : SRV02
FolderName                  : RF01
GroupDomainName             : corp.contoso.com
ComputerDomainName          : corp.contoso.com
Identifier                  : 6afad5e2-366c-4210-ae0f-e94a03b2b628
DistinguishedName           : CN=72c0c2bc-8a4e-4984-a23c-2efadc238724,CN=ce80cd1c-40dd-4e43-89fa-f3ad78988f9a,CN=DFSR-L
                              ocalSettings,CN=SRV02,OU=Domain Controllers,DC=corp,DC=contoso,DC=com
ContentPath                 : c:\rf01
PrimaryMember               : False
StagingPath                 : c:\rf01\DfsrPrivate\Staging
StagingPathQuotaInMB        : 4096
MinimumStagingFileSize      : Size256KB
ConflictAndDeletedPath      : c:\rf01\DfsrPrivate\ConflictAndDeleted
ConflictAndDeletedQuotaInMB : 660
ReadOnly                    : False
RemoveDeletedFiles          : False
Enabled                     : True
DfsnPath                    :
State                       : Normal
```

该命令会获取所有复制组中的所有成员计算机信息。控制台显示了两台名为 SRV01 和 SRV02 的成员计算机的 **DfsrMembership** 对象。这两台计算机属于同一个名为 RG01 的组。

## 参数

### -ComputerName
指定一组复制成员计算机的名称。该cmdlet会修改这些成员计算机的成员资格设置。您可以使用逗号分隔的列表以及通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: MemberList, MemList

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: True
```

### -DomainName
指定包含复制组的 Active Directory 域服务（AD DS）域的 NetBIOS 名称或完全限定域名（FQDN）。如果您未指定此参数，该 cmdlet 将使用当前用户的域。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 100
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -GroupName
指定一个复制组名称的数组。如果不指定此参数，该cmdlet将适用于所有参与的复制组。您可以使用逗号分隔的列表以及通配符（*）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: RG, RgName

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: True
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.DistributedFileSystemReplication.DfsReplicationGroup

## 输出

### Microsoft.DistributedFileSystemReplication.DfsrMembership

## 备注

## 相关链接

[Set-DfsrMembership](./Set-DfsrMembership.md)

[Add-DfsrMember](./Add-DfsrMember.md)

